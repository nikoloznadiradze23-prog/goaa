function App(){
    const[user, setUser] = useState("");
    const handleSubmit = (e) => {
        e.preventDefault();
        setUser(e.target.element.value)
    }
    <>
        return(
            <form onSubmit={handleSubmit}>
                <input placeholder="user"></input>
            </form>
            <h2>Tasks</h2>
            <ul>
                {task.map((task) => <li key={index}>{Value}</li>)}
            </ul>
        )
    </>
}