const redis = require('redis')
const client = redis.createClient()

client.on('error', (err) => {
  console.log('redis error', err)
})

class RedisClient {
  /** set */
  static set (key, value, expire) {
    if (expire) {
      client.set(key, value, 'EX', expire)
      return
    }
    client.set(key, value)
  }

  /** get */
  static get (key) {
    return new Promise((resolve, reject) => {
      client.get(key, (err, reply) => {
        if (err) return reject(err)
        resolve(reply)
      })
    })
  }
}

RedisClient.set('aaa', 'aaa', 10)
// RedisClient.get('aaa').then(msg => {
//   console.log(msg)
// })
