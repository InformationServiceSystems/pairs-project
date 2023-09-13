const debug = require('debug')('app')
const OpenApiValidator = require('express-openapi-validator');
const express = require('express')
const cors = require('cors')
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');


(async () => {


    const port = process.env.PORT || 8080
    const server = express()
    server.use(bodyParser())

    //cors
    var corsOptionsDelegate = function (req, callback) {
        var corsOptions = {
            "origin": "*",
            "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
            "preflightContinue": false,
            "optionsSuccessStatus": 204
        }
        callback(null, corsOptions) // callback expects two parameters: error and options
    }
    server.use(cors(corsOptionsDelegate))
    server.use(express.json())
    server.use(express.urlencoded({extended: true}))

    //openapi definitions
    // server.use(
    //     OpenApiValidator.middleware({
    //         apiSpec: './openapi.yaml',
    //         validateRequests: true,
    //         validateResponses: true,
    //         formats: require('./api/utils/formats'),
    //         validateSecurity: {
    //             handlers: require('./api/utils/authentication')
    //         },
    //         $refParser: {
    //             mode: 'dereference'
    //         }
    //     }),
    // );


    server.use(fileUpload());
    server.use('/example', require("./src/http/example"))
    server.use('/interface', require("./src/http/interface"))


    server.listen(port, "0.0.0.0", () => debug(`Node listening on port ${port}`))

    server.use((err, req, res, next) => {
        // format error
        res.status(err.status || 500).json({
            message: err.message,
            errors: err.errors,
        });

    });
})()
