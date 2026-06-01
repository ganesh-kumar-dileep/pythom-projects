from flask import Flask, jsonify, request

app = Flask(__name__)

car_state = "s"
distance = 100
pre_error = 0
flag = 0
distanceL = 0
distanceR = 0
@app.route("/distance", methods=["POST"])
def receive_distance():
    data = request.get_json()
    global distance
    distance = data.get("distance")

    print(f"Distance received: {distance} cm")

    return jsonify({"message": "distance received", "distance": distance})


@app.route("/data", methods=["GET"])
def set_car():

    global car_state
    global distance
    

    minpwm = 125
    error, output = pd_controller()
    if distance >= 20 and distance <= 30:
        car_state = "oa"
        output = 0

    elif error > 5:
        car_state = "f"
        if output < minpwm:
            output = minpwm
    elif error < -5:
        car_state = "r"
        if output < minpwm:
            output = minpwm
    
    
    print(f"distance: {distance}, error: {error}, output: {output}")
    
    return jsonify({"status": car_state, "pwm": output})

def pd_controller():
    global distance
    global pre_error
    target = 25
    dt = 0.2
    error = distance - target
    derivative = (error - pre_error) / dt
    kp = 4
    kd = 0.7
    output = (kp * error) + (kd * derivative)
    maxSpeed = 150
    if output > maxSpeed:
        output = maxSpeed
    pre_error = error
    return error, output

def obastacle_avoid():
    global distance
    global car_state
    
    return car_state

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)