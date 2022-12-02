import React from "react"
import LoginForm from "./components/LoginForm"
import { UserProvider } from "./components/UserContext";

const App = () => {
  return (
    <UserProvider>
      <LoginForm />
    </UserProvider>
  )
}

export default App;