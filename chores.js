var twilio = require('twilio')
var schedule = require('node-schedule');
var readline = require('readline');
var config = require('./config.json')

chores = {
  'd': 60,
  'w': 40,
  'dishwasher': 60,
  'test': 1
}

var sendSms = function(task){
  var accountSid = config['twilio']['account_sid']
  var authToken = config['twilio']['auth_token']
  var client = new twilio.RestClient(accountSid, authToken)
  client.messages.create({
    body: `Your ${task} is done`,
    to: '5163616129',
    from: '+15168744020'
  }, function(err, message) {
    if (err) {
      console.log(err.message)
    }
    console.log(message.sid);
    process.exit(0);
  });
};

var read = function(){
  var rl = readline.createInterface(process.stdin, process.stdout);
  rl.setPrompt('What is the task? (d, w, dishwasher)\n');
  rl.prompt();
  rl.on('line', function(line) {
    setTimeout(sendSms, chores[line]*1000*60, line)
  });
};
read()
