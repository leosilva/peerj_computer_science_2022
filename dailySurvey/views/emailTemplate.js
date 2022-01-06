module.exports = {
    getTemplate: function(randomHash, userId) {
        return `
            <div id="body" style="width: 80%; margin: auto; border: 2px solid black; border-radius: 5px;">
                <div id="header" style="text-align: center;">
                    <img src="cid:uc-logo" alt="UC Logo" title="UC Logo" />
                </div>
                <p style="font-size: 14pt; padding: 10px;">This is an automatic email from a University of Coimbra research. 
                As a participant of this research, we would like you to answer the survey below. Please, answer only once per email received.</p>
                <div id="form" style="width: 70%; margin: auto; padding: 15px;">
                    <h1 style='text-align: center; margin-bottom: 40px;'>Online Daily Survey</h1>
                    <form action='http://localhost:8080/survey/answer' method='post'>
                        <div id="div-q1" style="margin-bottom: 30px;">
                            <label for='q1' style="font-weight: bold; font-size: large; display: block; margin-bottom: 20px;">1 - How do you feel in this moment?</label>
                            <div style="display: flex; justify-content: center; align-items: center;">
                                <input type='radio' id="very-unhappy" name='q1' value="very-unhappy">
                                <label for="very-unhappy"><img src="cid:very-unhappy" style="height: 70px; width: 70px;" alt="Very Unhappy" title="Very Unhappy"></label>
                                <input type='radio' id="unhappy" name='q1' value="unhappy">
                                <label for="unhappy"><img src="cid:unhappy" style="height: 70px; width: 70px;" alt="Unhappy" title="Unhappy"></label>
                                <input type='radio' id="neutral" name='q1' value="neutral">
                                <label for="neutral"><img src="cid:neutral" style="height: 70px; width: 70px;" alt="Neutral" title="Neutral"></label>
                                <input type='radio' id="happy" name='q1' value="happy">
                                <label for="happy"><img src="cid:happy" style="height: 70px; width: 70px;" alt="Happy" title="Happy"></label>
                                <input type='radio' id="very-happy" name='q1' value="very-happy">
                                <label for="very-happy"><img src="cid:very-happy" style="height: 70px; width: 70px;" alt="Very Happy" title="Very Happy"></label>
                            </div>
                        </div>
                        <div id="div-q2" style="margin-bottom: 30px;">
                            <label for='q2' style="font-weight: bold; font-size: large; display: block; margin-bottom: 20px;">2 - Was there any meaningful event, work-related or not, in the last 24 hours?</label>
                            <div style="display: flex; justify-content: center; align-items: center;">
                                <textarea name="q2" rows="5" cols="100"></textarea>
                            </div>
                        </div>
                        <div id="div-q3" style="margin-bottom: 30px;">
                            <label for='q3' style="font-weight: bold; font-size: large; display: block; margin-bottom: 20px;">3 - If so, do you consider this event to be positive or negative?</label>
                            <div id="q3">
                                <div style="display: block">
                                    <input type='radio' id="positive" name='q3' value="positive">
                                    <label for="positive">Positive</label>
                                </div>
                                <div style="display: block">
                                    <input type='radio' id="negative" name='q3' value="negative">
                                    <label for="negative">Negative</label>
                                </div>
                            </div>
                        </div>
                        <div id="buttons">
                            <input type='submit' value='Submit' style="
                            color: black;
                            background-color: transparent;
                            outline:0;
                            width: 100px;
                            padding: 10px;
                            font-size: 1em;
                            border: 2px solid darkblue;
                            border-radius: 5px;
                            cursor: pointer;">
                        </div>
                        <input type="hidden" name="userId" value=\"${userId}\">
                        <input type="hidden" name="uniqueKeyUserSession" value=\"${randomHash}\">
                    </form>
                </div>
            </div>
            `
    }
}