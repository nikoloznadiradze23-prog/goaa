// function Greeting ({children, username}) {
//     return(
//         <div style={ {border:"3px solid black"}}>
//             {children}
//             <p>hello {username || "john doe"}</p>
//         </div>
//     )
// }



function app(){
    const[count, setCount] = useState(0)
    // let count = 0;
    function handlein(){
        count++
    }
    function handlede(){
        count--;

    }
    return(
        <>
        <button onClick={() => setCount((prev) => + 1)}> increment +1</button>
        <button onClick={() => setCount((prev) => - 1)}> increment -1</button>
        <br/>
        <p>Count: {count}</p>
        </>
    )
}