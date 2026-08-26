import Component3 from "./component3"
import { useContext } from "react"
export default function Component (){
    const [name, setName] = useState("nika")

    return(
        <div className="componentDiv">
            <h2>component 2</h2>
            <Component3/>
        </div>
    )
}