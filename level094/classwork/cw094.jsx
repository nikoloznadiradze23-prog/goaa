import React, {useMemo, useState} from "react";

function expensive(a) {
    for(let i = 0; i < 100000; i++){}
    return a * 2
}

export default function App(){
    const [num1, setNum1] = useState(1)
    const [num2, setNum2] = useState(1)
    const [doubled, setDoubled] = useState(num2)

    const getDouble = useMemo(() => expensive(num2), num2)

    return (
        <>
            <button onClick={() => setNum1((prev) => prev + 1)}>add one to number 1</button>
            <p>number one: {num1}</p>

            <button onClick={() => setNum2((prev) => prev + 1)}>add one to number 2</button>
            <p>number two: {num2}</p>

            <button onClick={() => setDoubled(getDouble)}>double number 2</button>
        </>
    )
}