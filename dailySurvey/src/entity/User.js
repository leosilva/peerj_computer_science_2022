var EntitySchema = require("typeorm").EntitySchema;

module.exports = new EntitySchema({
    name: "User", // Will use table name `category` as default behaviour.
    tableName: "User", // Optional: Provide `tableName` property to override the default behaviour for table name.
    columns: {
        id: {
            primary: true,
            type: "int",
            generated: true
        },
        id_str_twitter: {
            type: "varchar"
        },
        participant_id: {
            type: "int"
        },
        name: {
            type: "varchar"
        },
        screen_name: {
            type: "varchar"
        },
        email: {
            type: "varchar"
        }
    },
    relations: {
        surveys: {
            target: "Survey",
            type: "one-to-many",
            cascade: true
        }
    }
});