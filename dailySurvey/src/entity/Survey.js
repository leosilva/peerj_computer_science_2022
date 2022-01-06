var EntitySchema = require("typeorm").EntitySchema;

module.exports = new EntitySchema({
    name: "Survey", // Will use table name `post` as default behaviour.
    tableName: "Survey", // Optional: Provide `tableName` property to override the default behaviour for table name.
    columns: {
        id: {
            primary: true,
            type: "int",
            generated: true
        },
        q1: {
            type: "varchar",
            nullable: true
        },
        q2: {
            type: "text",
            nullable: true
        },
        q3: {
            type: "varchar",
            nullable: true
        },
        sendDate: {
            type: "datetime"
        },
        answerDate: {
            type: "datetime",
            nullable: true
        },
        securityHash: {
            type: "varchar",
            unique: true
        }
    },
    relations: {
        user: {
            target: "User",
            type: "many-to-one",
            cascade: true
        }
    }
})