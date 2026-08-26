const express = require('express')
const App = express()
const port = 3000
const products = [
    {"id":1111, "products": "orange", "name": "orange", "price": 2},
    {"id":2222, "products": "apple", "name": "apple", "price":1},
    
]

App.get("/products/", (req, res) => {
    res.json(products)
}) 
App.get("/products/:id", (req, res) => {
    const {id} = req.params;
    const products = products.find((p) => p.id === parseInt(id))
    if (products) {
        return res.status(200).json(products)
    }
    res.status(404).json({message: 'davdzebne da ar iyo'})
}) 
App.post('/products', (req,res) => {
    const {name, price} = req.body;
    if(!name|| !price){
        return res.staus(404).json({message: 'chepea chepe'})
    }
})
App.delete('/products/:id', (req, res) => {
    const {id} = req.params;
    const productsIndex = products.findIndex((prod) => prod.id === params)
    if(products === -1) {
        return res.status(404).send(`product with ${id} couldnot find by id`)
    }
    const filteredproducts = products.filter((prod) => prod.id)
    products = filteredproducts;
    res.status(204).send('removed successfuly')
})
App
App.listen(3000)