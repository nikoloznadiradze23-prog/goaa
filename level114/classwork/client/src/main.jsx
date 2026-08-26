import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { useContext } from 'react'
import authContext from './context/authContext.jsx'
import { auth } from './context/authcontext.jsx'
import {authContextProvider} from './context/authcontext.jsx'
const authContext = useContext(authContext)

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <auth>
      <App />
    </auth>
  </StrictMode>,
)
