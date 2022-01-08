const express = require("express")
const surveyController = require("./controllers/SurveyController")
const taskScheduler = require("./services/TaskScheduler")
const joi = require("joi")
const typeorm = require("typeorm"); // used for validation
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/images'));
app.set("view engine", "ejs");

const connection = typeorm.createConnection();

app.put("/api/survey",  (req, res) => {
    // console.log(req.body)
    surveyController.sendSurvey()
    res.status(200).send("Email sent succesfully!")
})

app.post("/survey/answer", async (req, res) => {
    let result = await surveyController.updateSurvey(req.body)
    if (result == "success") {
        res.status(200).sendFile('views/thank_you.html', {root: __dirname })
    } else {
        res.render("error", {message: result})
    }
})

const port = process.env.PORT || 8080
app.listen(port, () => console.log(`listening on port ${port}...`))
console.log(process.env)

taskScheduler.scheduleSendEmail()