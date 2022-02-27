import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "pages/Home";
import Header from "components/Header";
import Likes from "pages/Likes";
import { useRecoilState } from "recoil";
import { userInfoState } from "state/atom";
import axios from "axios";
import Detail from "pages/Detail";

function App() {
  const access_token =
    localStorage.access_token ||
    window.location.hash.split("&")[0].split("=")[1];

  const [userInfo, setUserInfo] = useRecoilState(userInfoState);
  const handleUserInfoChange = useCallback((info) => {
    setUserInfo(info);
  }, []);

  const asyncGetUserInfo = async (token) => {
    try {
      const { data: res } = await axios.get(
        `https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=${token}`
      );
      if (Object.keys(res).length) {
        handleUserInfoChange(res);
        window.history.replaceState({}, null, "/");
        await axios.post(
          "http://192.168.219.108:50001/user_info/info",
          { name: res.name, email: res.email },
          {
            headers: {
              "Content-Type": `application/json`,
            },
          }
        );
      }
    } catch (e) {
      console.error(e);
    }
  };
  useEffect(() => {
    if (access_token) {
      localStorage.setItem("access_token", access_token);
      asyncGetUserInfo(access_token);
    }
  }, [access_token]);

  return (
    <Router>
      <Header userInfo={userInfo} />
      <Switch>
        <Route
          path="/"
          exact
          render={() => <Home handleUserInfoChange={handleUserInfoChange} />}
        />
        <Route path="/likes" render={() => <Likes />} />
        <Route path="/hotel/:_id" component={Detail} />
      </Switch>
    </Router>
  );



export default App;
