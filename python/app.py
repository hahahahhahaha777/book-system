from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    facilities = [
        {"name": "Badminton Gym", "price": 15.00, "image": "BadmintonGym.jpg"},
        {"name": "Berball", "price": 10.00, "image": "Berball.jpg"},
        {"name": "Boxing", "price": 10.00, "image": "Boxing.jpg"},
        {"name": "Running Machine", "price": 15.00, "image": "RunningMachine.jpg"},
        {"name": "Spinning", "price": 15.00, "image": "Spinning.jpg"},
        {"name": "Swimming Pool", "price": 10.00, "image": "SwimmingPool.jpg"},
        {"name": "Tennis Stadium", "price": 15.00, "image": "TennisStadium.jpg"},
        {"name": "Dancing Studio", "price": 5.00, "image": "DancingStudio.jpg"},
        {"name": "Nutrition Counseling", "price": 15.00, "image": "NutritionCounseling.jpg"},
        {"name": "Sports Physiotherapy", "price": 10.00, "image": "SportsPhysiotherapy.jpg"}
        # Add more facilities as needed
    ]
    return render_template('index.html', facilities=facilities)

if __name__ == '__main__':
    app.run(debug=True)
