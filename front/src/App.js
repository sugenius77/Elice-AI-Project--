import "./App.css";
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import Home from "pages/Home";
import Register from "pages/Register";
import Login from "pages/Login";
import Header from "components/Header";

function App() {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path="/" exact render={() => <Home />} />
                <Route path="/login" render={() => <Login />} />
                {/* <Route path="/register" render={() => <Register />} /> */}
                <Route path={"/register"} component={Register} />
            </Switch>
        </Router>
    );
}

export default App;
