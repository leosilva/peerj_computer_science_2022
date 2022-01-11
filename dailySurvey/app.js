const express = require("express")
const surveyController = require("./controllers/SurveyController")
const taskScheduler = require("./services/TaskScheduler")
const joi = require("joi")
const typeorm = require("typeorm"); // used for validation
const { getBaseUrl } = require("get-base-url")
const surveyTemplate = require("./views/survey/survey")

const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/images'));
app.set("view engine", "ejs");

const connection = typeorm.createConnection();

app.put("/api/survey",  (req, res) => {
    surveyController.sendSurvey()
    res.status(200).send("Email sent succesfully!")
})

app.post("/survey/api/answer", async (req, res) => {
    let result = await surveyController.updateSurvey(req.body)
    if (result == "success") {
        res.status(200).sendFile('views/thank_you.html', {root: __dirname })
    } else {
        res.render("error", {message: result})
    }
})

app.get("/survey/web/answer", (req, res) => {
    console.log("acessing the web version of the survey...")
    res.render("survey/webSurvey", {
        surveyTemplate: surveyTemplate.getTemplate(req.query.randomHash,
            req.query.userId,
            true)
        })
})

const port = process.env.PORT || 8080
app.listen(port, () => console.log(`listening on port ${port}...`))

taskScheduler.scheduleSendEmail()