const express = require("express")
const surveyController = require("./controllers/SurveyController")
const joi = require("joi") // used for validation
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/images'));


app.put("/api/survey", (req, res) => {
    surveyController.sendSurvey()
    res.status(200).send("Email sent succesfully!")
})

app.post("/survey/answer", (req, res) => {
    console.log(req.body)
    res.sendFile('views/thank_you.html', {root: __dirname })
})

app.put("/api/user/create", async (req, res) => {
    // const connection = typeorm.createConnection();
    // connection.then(async function (conn) {
    //     const userRepository = conn.getRepository("User");
    //     // var user = {
    //     //     firstName: "Timber",
    //     //     lastName: "Saw",
    //     //     age: 25
    //     // };
    //     //
    //     // await userRepository.save(user);
    //     //
    //     const allUsers = await userRepository.find();
    //     console.log(allUsers)
    //     // const firstUser = await userRepository.findOne(1); // find by id
    //     // const timber = await userRepository.findOne({firstName: "Timber", lastName: "Saw"});
    // })
    // await repository.remove(timber);
    surveyController.sendSurvey()
    res.send("OK")
})

const port = process.env.PORT || 8080
app.listen(port, () => console.log(`listening on port ${port}...`))