"""
Service API endpoints
"""

from flask import Flask, request, jsonify, make_response
import Orchestrator
import Params
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

orchestrator = Orchestrator.Orchestrator()

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    # Ping endpoint
    return make_response(jsonify("YouLearn server is up!"), 200)

@app.route("/api/filterDistractfulVideos", methods=["POST"])
@cross_origin()
def filter_videos():
    """
    Endpoint to filter distractful videos
    input:  list of ids of recommended videos
    output: list of ids of distractful videos
    """

    data = request.get_json()
    recommended_videos_ids_list = data['recommended_ids']

    u = orchestrator.filter_distractful(recommended_videos_ids_list)
    return u if u else make_response(jsonify(u), 500)
    
@app.route("/api/filterAndSortDistractfulVideos", methods=["POST"])
@cross_origin()
def filter_and_sort_videos():
    """
    Endpoint to filter and sort distractful videos
    input:  list of ids of recommended videos
    output: list of ids of sorted recommended videos
    """

    filter_threshold = request.args.get("filter_threshold")

    if filter_threshold is None:
        filter_threshold = 0.5
    else:
        filter_threshold = float(filter_threshold)

    data = request.get_json()
    recommended_videos_ids_list = data['recommended_ids']

    u = orchestrator.filter_and_sort_distractful(filter_threshold, recommended_videos_ids_list)
    return u if u else make_response(jsonify(u), 500)

@app.route("/api/feedback", methods=["POST"])
@cross_origin()
def feedback():
    """
    Endpoint to post feedback
    input: video_id, helpful boolean
    output: confirmation?
    """

    data = request.get_json()
    video_id = data['video_id']
    is_distractful = data['distractful'] # boolean distractful: true or false
    
    u = orchestrator.feedback(video_id, is_distractful)
    return jsonify("Feedback for video "+video_id+" stored.") if u else make_response(jsonify(u), 500)


# TODO
@app.route("/api/get_recommendations", methods=["POST"])
@cross_origin()
def get_recommendations():
    """
    Endpoint to return ids of videos to be recommended
    """

    return None

    data = request.get_json()
    u = orchestrator.get_recommendations(userId, video_url)
    return jsonify(u) if u else make_response(jsonify(u), 500)



if __name__ == "__main__":
    if eval(Params.RUNNING_IN_CLOUD):
        app.run(host='0.0.0.0', port=80, debug=True)
    else:
        app.run(debug=True)  # run the Flask app