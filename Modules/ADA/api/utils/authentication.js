let authentication = {}

authentication.BasicUser = async function (req, scopes, schema) {
    try {
        // add authentication here!
        return true
    } catch (err) {
        throw { status: 401, message: 'Unauthorized: ' + err.message }
    }
}


module.exports = authentication