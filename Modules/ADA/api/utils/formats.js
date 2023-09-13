let formats = []

const regex = {
    ip: /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/
}

for (const [name, testRegex] of Object.entries(regex)) {
    formats.push(
        {
            name,
            type: 'string',
            validate: (value) => testRegex.test(value)
        }
    )
}

module.exports = formats