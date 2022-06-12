"""
Service API endpoints
"""

from flask import Flask, request, jsonify, make_response
import Orchestrator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Ping endpoint
    return make_response(jsonify("YouLearn server is up!"), 200)

@app.route("/api/filterDistractfulVideos", methods=["POST"])
def filter_videos():
    """
    Endpoint to filter distractful videos
    input:  list of ids of recommended videos
    output: list of ids of distractful videos
    """

    data = request.get_json()
    recommended_videos_ids_list = data['recommended_ids']

    u = Orchestrator.filter_distractful(recommended_videos_ids_list)
    return u if u else make_response(jsonify(u), 500)
    

# TODO
@app.route("/api/feedback", methods=["POST"])
def feedback():
    """
    Endpoint to post feedback
    input: video_id, helpful boolean
    output: confirmation?
    """
    return None
    
    data = request.get_json()
    video_id = data['video_id']
    feedback = data['distractful'] # boolean helpful: true or false
    
    u = Orchestrator.feedback(video_id, feedback)
    return jsonify(u) if u else make_response(jsonify(u), 500)


# TODO
@app.route("/api/get_recommendations", methods=["POST"])
def get_recommendations():
    """
    Endpoint to return ids of videos to be recommended
    """
    return None

    data = request.get_json()
    u = Orchestrator.get_recommendations(userId, video_url)
    return jsonify(u) if u else make_response(jsonify(u), 500)

if __name__ == "__main__":
    app.run(debug=True)  # run the Flask app