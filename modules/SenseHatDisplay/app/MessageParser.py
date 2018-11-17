class MessageParser:
    #Returns the highest probablity tag in the json object (takes the output as json.loads as input)
    def highestProbabilityTagMeetingThreshold(self, predictionResult, threshold):
        highestProbabilityTag = 'none'
        highestProbability = 0
        allTagsAndProbability = predictionResult['predictions']
        for item in allTagsAndProbability:
            if item['probability'] > highestProbability and item['probability'] > threshold:
                highestProbability = item['probability']
                highestProbabilityTag = item['tagName']
        return highestProbabilityTag