const express = require('express')
const main = express()
const port = 3000
const parts = [
    {"id":1111, "part": "gpu", "name": "nvidea", "price": 529},
    {"id":2222, "part": "cpu", "name": "intel", "price":320},
    
]

main.get("/parts/", (req, res) => {
    res.json(parts)
}) 
main.get("/parts/:id", (req, res) => {
    const {id} = req.params;
    const parts = parts.find((p) => p.id === parseInt(id))
    if (parts) {
        return res.status(200).json(parts)
    }
    res.status(404).json({message: 'davdzebne da ar iyo'})
}) 
main.post('/parts', (req,res) => {
    const {name, price} = req.body;
    if(!name|| !price){
        return res.staus(404).json({message: 'chepea chepe'})
    }
})
main.delete('/parts/:id', (req, res) => {
    const {id} = req.params;
    const partsIndex = parts.findIndex((prod) => prod.id === params)
    if(partsIndex === -1) {
        return res.status(404).send(`product with ${id} couldnot find by id`)
    }
    const filteredParts = parts.filter((prod) => prod.id)
    parts = filteredParts;
    res.status(204).send('removed successfuly')
})
main
main.listen(3000)