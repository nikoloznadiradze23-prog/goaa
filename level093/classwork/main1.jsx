import React from "react";

export default class ErrorBoundary extends React.Component{
    constructor (props){
        super(props)
    }
    state = { hasError: false}
    static getDerivedStateFromError(){
        state.hasError - true
    }
    static componentDidCatch(error, info){
        console.log(error, info)
    }
    render(){
        if (this.state.hasError){
            return <p>Fallback UI...</p>
        }else{
            this.children
        }
    }
}