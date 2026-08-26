import Component4 from "./component4.jsx"
import { useContext } from "react"
export default function Component (){
    const [name, setName] = useState("nika")

    return(
        <div className="componentDiv">
            <h2>component3</h2>
            <Component4/>
        </div>
    )
}