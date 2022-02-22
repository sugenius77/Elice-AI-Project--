import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "pages/Home";
import Register from "pages/Register";
import Login from "pages/Login";
import Header from "components/Header";
import Detail from "pages/Detail";

function App() {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path="/" exact render={() => <Home />} />
                <Route path="/login" render={() => <Login />} />
                <Route path={"/register"} component={Register} />
                <Route path="/hotel/:_id" component={Detail} />
            </Switch>
        </Router>
    );
}

export default App;
