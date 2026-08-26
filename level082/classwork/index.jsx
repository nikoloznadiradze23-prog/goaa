import { useState, useEffect } from "react";
function App(){}{
    const [count, setCount] = useState(0);
    useEffect(() => {
        fetch('')
            .then(Response => Response.json())
            .then(data => setCount(data.count))
    })
}