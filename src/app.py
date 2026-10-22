from flask import Flask, jsonify, request
from .shipping import calculate_shipping

def create_app():
    app = Flask(__name__)
    
    @app.route('/shipping', methods=['POST'])
    def calculate_shipping_endpoint():
        """Calculate shipping cost based on order total."""
        try:
            data = request.get_json()
            if not data or 'order_total' not in data:
                return jsonify({'error': 'order_total is required'}), 400
            
            order_total = float(data['order_total'])
            shipping_cost = calculate_shipping(order_total)
            
            return jsonify({
                'order_total': order_total,
                'shipping_rate': 0.10,
                'shipping_cost': shipping_cost,
                'message': f'Shipping calculated at 10% rate: ${shipping_cost:.2f}'
            })
        except ValueError:
            return jsonify({'error': 'order_total must be a number'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)