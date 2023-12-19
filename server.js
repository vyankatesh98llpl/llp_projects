const express = require('express');
const app = express();
const port = 3000; // You can use any port you prefer
const bodyParser = require('body-parser');
const calci = require('./calcis');


const { Addition,  substration, multiplication, Divion } = require('./calcis');
app.use(bodyParser.json());
app.post('/adds', calci.Addition);
app.post('/subtract', calci.substration);
app.post('/multiply', calci.multiplication);
app.post('/divide', calci.Divion);

const { add_update,sub_update,mul_update,div_update } = require('./calcis');

app.put('/updtadd/:id', calci.add_update);
app.put('/updtsub/:id', calci.sub_update);
app.put('/updtmul/:id', calci.mul_update);
app.put('/updtdiv/:id', calci.div_update);

const { add_delete,sub_delete,mul_delete,div_delete } = require('./calcis');
app.delete('/deleteadd/:id', calci.add_delete);
app.delete('/deletesub/:id', calci.sub_delete);
app.delete('/deletemul/:id', calci.mul_delete);
app.delete('/deletediv/:id', calci.div_delete);

// Start the server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});


