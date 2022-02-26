import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useRecoilState } from "recoil";
import { userInfoState } from "state/atom";
const menuItems = [
  {
    title: "Search",
    key: "/",
    index: 1,
  },
  {
    title: "Login",
    key: "/callback",
    index: 2,
  },
];

const Header = () => {
  const [userInfo, setUserInfo] = useRecoilState(userInfoState);
  const [showMenu, setShowMenu] = useState(false);
  const handleMenuToggle = () => {
    setShowMenu((prev) => !prev);
  };
  const handleMenuClose = () => {
    setShowMenu(false);
  };

  return (
    <div className="font-doogle text-white w-full z-50">
      <div
        className={`flex justify-between bg-theme opacity-50 items-center p-2 shadow-lg `}
      >
        <div className="flex justify-between w-full">
          <Link to="/" className="text-4xl font-semibold mb-2">
            H O T E L S
          </Link>
        </div>
        <div className="flex items-center">
          {userInfo.name ? (
            <>
              <li className="list-none mx-2 p-1">
                <Link to="/" key="1">
                  Search
                </Link>
              </li>
              <li className="list-none mx-2 p-1">
                <div className="dropdown">
                  <button
                    onClick={handleMenuToggle}
                    type="button"
                    className="flex z-10 flex items-center border-transparent rounded-full focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white cursor-not-allowe"
                  >
                    <img
                      className="flex  max-w-md h-10 w-10 rounded-full ring-3"
                      src={userInfo.picture}
                    />
                  </button>
                  {showMenu && (
                    <div
                      onClick={handleMenuClose}
                      className="w-full h-full inset-0 absolute"
                    >
                      <div className="absolute top-12 right-0 z-20 w-56 py-2 mt-2 overflow-hidden bg-white rounded-md shadow-xl dark:bg-gray-800">
                        <div className="flex items-center p-3 -mt-2 text-sm text-gray-600 transition-colors duration-200 transform dark:text-gray-300 ">
                          <div className="mx-1">
                            <h1 className="text-sm font-semibold text-gray-700 dark:text-gray-200">
                              {userInfo.name}
                            </h1>
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                              {userInfo.email}
                            </p>
                          </div>
                        </div>
                        <a
                          className="flex items-center px-3 py-3 cursor-pointer hover:bg-gray-600 font-light text-sm focus:outline-none"
                          href="/likes"
                        >
                          <div className="mr-2">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              className="h-5 w-5"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                            >
                              <path
                                fill-rule="evenodd"
                                d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
                                clip-rule="evenodd"
                              />
                            </svg>
                          </div>
                          My Favorite
                        </a>
                        <div
                          className="flex items-center px-3 py-3 cursor-pointer hover:bg-gray-600 font-light text-sm focus:outline-none"
                          onClick={() => {
                            setUserInfo({});
                            localStorage.clear();
                          }}
                        >
                          {" "}
                          <div className="mr-2">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              className="h-6 w-6"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3  013-3h4a3 3 0 013 3v1"
                              />
                            </svg>
                          </div>
                          Logout
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </li>
            </>
          ) : (
            menuItems.map((item) => {
              if (item.index === 2) {
                return (
                  <li
                    className="list-none mx-2 p-1"
                    onClick={() =>
                      (window.location.href =
                        "https://accounts.google.com/o/oauth2/v2/auth?" +
                        "client_id=" +
                        "944228758716-ik6sa442kp2ielcg2pqbi5npocgqkq1n.apps.googleusercontent.com" +
                        "&response_type=token" +
                        //"&access_type=offline" +
                        "&redirect_uri=http://localhost:3000/&" +
                        "scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile")
                    }
                  >
                    {item.title}
                  </li>
                );
              }
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                />
              </svg>;
              return (
                <li className="list-none mx-2 p-1">
                  <Link to={item.key} key={item.index}>
                    {item.title}
                  </Link>
                </li>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
};

export default Header;
