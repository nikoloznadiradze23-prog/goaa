import Component2 from "./component2"
import { useState, createContext } from "react"

export const nameContext = createContext();
export default function Component (){
    const [name, setName] = useState("nika");

    return(
        <div className="componentDiv">
            <h2>component 1</h2>
            <nameContext.Provider name={name}>
                <Component2/>
            </nameContext.Provider>
            
        </div>
    )
}