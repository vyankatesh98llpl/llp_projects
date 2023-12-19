const prompt=require("prompt-sync")({sigint:true}); 
const { json } = require("express");
const mysql = require('mysql');

const pool  = mysql.createPool({
    host: 'localhost',
    user: 'root',
    port: 3306,
    password: 'password',
    database: 'calci',
    waitForConnections: true,
    connectionLimit: 10,
  });

  
function Addition(req, res){
    const {a , b} = req.body;
    console.log(req.body)
    const value1 = req.body;
    results = a + b;
    his = ([a, '+' , b ,'=', results]);
    
    const sql = 'INSERT INTO calci.add (result, history) VALUES (?,? )'; 
    const values = [results, JSON.stringify(his)];
    pool.query(sql,values, (error, fields) => {
    if (error) {
      console.error('Error inserting into the database:', error);
      return res.status(500).send('Error inserting into the database');
    }       
      });
    res.json({ results });
    // console.log(results)
}
// [120,"+",85,"=",205]
// function add_update(req, res){
    // const { id } = req.params;
    // const { newData } = req.body;
    // const { result, history } = newData;
    // console.log(id);
    // console.log(newData);
    // console.log(result, history);
    // res.json({ newData });
  
    // const sql = 'UPDATE calci.add SET (result , history ) WHERE id = ?';
    // const values = [result, history, id];
  
    // pool.query(sql, values, (error, results, fields) => {
    //   if (error) {
    //     console.error('Error updating data:', error);
    //     return res.status(500).send('Error updating data');
    //   }
  
    //   res.status(200).send('Data updated successfully');
    // });
// }


function substration(req, res){
    const {a , b} = req.body;
    result = a - b;
    his = ([a, '-' , b ,'=',result]);
    res.json({ result, his });
    const sql = 'INSERT INTO sub (result, history) VALUES (?,? )';
    pool.query(sql,  [result,JSON.stringify(his)], (error, fields) => {
    if (error) {
      console.error('Error inserting into the database:', error);
      return res.status(500).send('Error inserting into the database');
    }       
      });

    
}

function multiplication(req, res){
    const {a , b} = req.body;
    result = a * b;
    // answer.push(result);
    his = ([a, '*' , b ,'=',result]);
    res.json({ result, his });
    const sql = 'INSERT INTO calci.mul (result, history) VALUES (?,? )';
    pool.query(sql,  [result,JSON.stringify(his)], (error, fields) => {
    if (error) {
      console.error('Error inserting into the database:', error);
      return res.status(500).send('Error inserting into the database');
    }       
      });
    pool.query('SELECT * FROM calci.mul ', (error, results, fields) => {
        if (error) throw error;
        console.log(results);
      });
    
}

function Divion(req, res){
    const {a , b} = req.body;
    result = a / b;
    his = ([a, '/' , b ,'=',result]);
    res.json({ result, his });
    const sql = 'INSERT INTO calci.div (result, history) VALUES (?,? )';
    pool.query(sql,  [result,JSON.stringify(his)], (error, fields) => {
    if (error) {
      console.error('Error inserting into the database:', error);
      return res.status(500).send('Error inserting into the database');
    }       
      });
    pool.query('SELECT * FROM calci.div ', (error, results, fields) => {
        if (error) throw error;
        console.log(results);
      });
    
}


pool.query('SELECT * FROM calci.add ', (error, results, fields) => {
  if (error) throw error;
  console.log(results);
});
pool.query('SELECT * FROM calci.sub ', (error, results, fields) => {
  if (error) throw error;
  console.log(results);
});




function add_update(req, res){
  const { id } = req.params;
  const { result, history } = req.body;
  console.log(id , result,history);
  const sql = 'UPDATE calci.add SET result = ?, history = ? WHERE id = ?';
  const values = [result, history, id];

  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data updated successfully');
  });
};

function sub_update(req, res){
  const { id } = req.params;
  const { result, history } = req.body;
  console.log(id , result,history);
  const sql = 'UPDATE calci.sub SET result = ?, history = ? WHERE id = ?';
  const values = [result, history, id];

  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data updated successfully');
  });
};

function mul_update(req, res){
  const { id } = req.params;
  const { result, history } = req.body;
  console.log(id , result,history);
  const sql = 'UPDATE calci.mul SET result = ?, history = ? WHERE id = ?';
  const values = [result, history, id];

  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data updated successfully');
  });
};

function div_update(req, res){
  const { id } = req.params;
  const { result, history } = req.body;
  console.log(id , result,history);
  const sql = 'UPDATE calci.div SET result = ?, history = ? WHERE id = ?';
  const values = [result, history, id];

  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data updated successfully');
  });
};



function add_delete(req, res){
  const { id } = req.params;
  console.log(id );
  const sql = 'DELETE from calci.add WHERE id = ?';
  const values = [id];
  
  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data Deleted successfully');
  });
};

function sub_delete(req, res){
  const { id } = req.params;
  console.log(id );
  const sql = 'DELETE from calci.sub WHERE id = ?';
  const values = [id];
  
  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data Deleted successfully');
  });
};
function mul_delete(req, res){
  const { id } = req.params;
  console.log(id );
  const sql = 'DELETE from calci.mul WHERE id = ?';
  const values = [id];
  
  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data Deleted successfully');
  });
};
function div_delete(req, res){
  const { id } = req.params;
  console.log(id );
  const sql = 'DELETE from calci.div WHERE id = ?';
  const values = [id];
  
  pool.query(sql, values, (error, results, fields) => {
    if (error) {
      console.error('Error updating data:', error);
      return res.status(500).send('Error updating data');
    }

    res.status(200).send('Data Deleted successfully');
  });
};


// const deleteQuery = 'UPDATE memory SET operation = ' +dataToUpdateItem +' WHERE id = ?';
module.exports = { Addition, substration, multiplication, Divion , add_update,sub_update,mul_update,div_update, add_delete,sub_delete,mul_delete,div_delete};
