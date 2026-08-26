import Component4 from "./component4"
import { useContext } from "react"
export default function Component (){
    const [name, setName] = useState("nika")

    return(
        <div className="componentDiv">
            <h2>component 3</h2>
            <Component4/>
        </div>
    )
}