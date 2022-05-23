"""
Service API endpoints
"""

from flask.wrappers import Response
from flask import Flask, request, jsonify, make_response
import Orchestrator
import json

app = Flask(__name__)

# Endpoint to get recommendations
# input: userID, videoUrl; output: list of urls to be recommended
@app.route("/api/getRecommendations", methods=['POST'])
def get_recommendations():
    data = request.get_json()
    user_id = data['user_id']
    video_url = data['video_url']

    u = Orchestrator.getRecommendations(user_id, video_url)
    return jsonify(u) if u else make_response(jsonify(u), 404)

# Endpoint to pass feedback for the recommended video
# input: userID, videoUrl, feedback (as string?); output: confirmation?
@app.route("/api/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    user_id = data['user_id']
    video_url = data['video_url']
    feedback = data['feedback']
    
    u = Orchestrator.feedback(user_id,video_url, feedback)
    return jsonify(u) if u else make_response(jsonify(u), 404)

if __name__ == "__main__":
    app.run(debug=True)  # run the Flask app