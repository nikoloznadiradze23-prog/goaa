    function addRandP() {
        let randN = Math.floor(Math.random() * 1000);
        let p = document.createElement("p");
        p.txt = "random " + randN;
        document.body.appendChild(p);
    }
