import WishList from "./WishList";
import React, { useState, Fragment } from "react";
import { Link, useLocation } from "react-router-dom";
import { Link as SLink } from "react-scroll";
import { useRecoilState } from "recoil";
import { userInfoState } from "../state/atom";
import { wishListState } from "../state/atom";
import { Dialog, Transition } from "@headlessui/react";
import { XIcon } from "@heroicons/react/outline";
import axios from "axios";

const menuItems = [
  {
    title: "Home",
    key: "/",
    index: 1,
  },
  {
    title: "Search",
    key: "/Search",
    index: 2,
  },
  {
    title: "Login",
    key: "/callback",
    index: 3,
  },
];

const Header = () => {
  const [open, setOpen] = useState(false);
  const location = useLocation();
  const pathname = location.pathname.slice(0, 6);
  console.log("pathname is header", pathname);
  const [userInfo, setUserInfo] = useRecoilState(userInfoState);
  const [wishList, setWishList] = useRecoilState(wishListState);
  const [showMenu, setShowMenu] = useState(false);
  const asyncGetHotels = async () => {
    try {
      const res = await axios.get(
        `${process.env.REACT_APP_API}/wish-list/${userInfo.id}`
      );
      setWishList(res.data.data);
    } catch (e) {
      console.error(e);
    }
  };
  const handleMenuToggle = () => {
    setShowMenu((prev) => !prev);
  };
  const handleMenuClose = () => {
    setShowMenu(false);
  };

  return (
    <>
      <div className="font-notoSans text-white fixed top-0 left-0 right-0 w-full z-50">
        <div
          className={`flex justify-between bg-[#2a5454] items-center p-2 shadow-lg `}
        >
          <div className="flex justify-between w-full">
            {pathname !== "/hotel" ? (
              <SLink
                to="1"
                spy={true}
                smooth={true}
                key="1"
                className="text-md font-semibold font-notoSans my-2 cursor-pointer"
              >
                {/* H O T E L S */}
                <div class="flex justify-center gap-1 my-1 w-full text-black">
                  <kbd className="kbd">H</kbd>
                  <kbd className="kbd">O</kbd>
                  <kbd className="kbd">T</kbd>
                  <kbd className="kbd">E</kbd>
                  <kbd className="kbd">L</kbd>
                </div>
              </SLink>
            ) : (
              <Link to="/" className="text-md font-semibold font-notoSans mb-2">
                {/* H O T E L S */}
                <div class="flex justify-center gap-1 my-1 w-full text-black">
                  <kbd className="kbd">H</kbd>
                  <kbd className="kbd">O</kbd>
                  <kbd className="kbd">T</kbd>
                  <kbd className="kbd">E</kbd>
                  <kbd className="kbd">L</kbd>
                </div>
              </Link>
            )}
          </div>
          <div className="flex items-center">
            {userInfo.name ? (
              <>
                <li className="list-none mx-2 p-1 cursor-pointer font-notoSans hover:scale-105 duration-150 md:hidden">
                  <SLink to="1" spy={true} smooth={true} key="1">
                    Home
                  </SLink>
                </li>
                <li className="list-none mx-2 p-1 cursor-pointer font-reviewsFont hover:scale-105 duration-150 md:hidden">
                  <SLink to="2" spy={true} smooth={true} key="2">
                    Search
                  </SLink>
                </li>
                <li className="list-none mx-2 p-1">
                  <div className="dropdown">
                    <button
                      onClick={handleMenuToggle}
                      type="button"
                      className="flex z-10 items-center border-transparent rounded-full focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white cursor-not-allowe"
                    >
                      <img
                        className="flex text-black max-w-md h-10 w-10 rounded-full ring-3"
                        src={userInfo.picture}
                        alt="google-login"
                      />
                    </button>
                    {showMenu && (
                      <div
                        onClick={handleMenuClose}
                        className="w-full h-full inset-0 absolute"
                      >
                        <div className="absolute top-12 text-black right-0 z-20 w-56 py-2 mt-2 overflow-hidden bg-white rounded-md shadow-xl ">
                          <div className="flex items-center p-3 -mt-2 text-sm text-gray-600 transition-colors duration-200 transform  ">
                            <div className="mx-1">
                              <h1 className="text-sm font-semibold text-gray-700 ">
                                {userInfo.name}
                              </h1>
                              <p className="text-sm text-gray-500 ">
                                {userInfo.email}
                              </p>
                            </div>
                          </div>
                          <div
                            onClick={() => {
                              setOpen(true);
                              asyncGetHotels();
                            }}
                            className="flex items-center px-3 py-3 cursor-pointer hover:bg-[#2a5454] hover:text-white font-light text-sm focus:outline-none"
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
                            Wish List
                          </div>
                          <div
                            className="flex items-center px-3 py-3 cursor-pointer hover:bg-[#2a5454] hover:text-white font-light text-sm focus:outline-none"
                            onClick={() => {
                              setUserInfo({});
                              localStorage.clear();
                              window.location.reload();
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
                if (item.index === 3) {
                  return (
                    <li
                      className="list-none mx-2 p-1 cursor-pointer hover:scale-105 duration-150"
                      onClick={() =>
                        (window.location.href =
                          "https://accounts.google.com/o/oauth2/v2/auth?" +
                          "client_id=" +
                          "944228758716-ik6sa442kp2ielcg2pqbi5npocgqkq1n.apps.googleusercontent.com" +
                          "&response_type=token" +
                          "&redirect_uri=http://localhost/&" +
                          "scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile")
                      }
                    >
                      {item.title}
                    </li>
                  );
                }
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
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                  />
                </svg>;
                return (
                  <li className="list-none mx-2 p-1 hover:scale-105 duration-150 md:hidden">
                    {pathname !== "/hotel" ? (
                      <SLink
                        to={item.index}
                        spy={true}
                        smooth={true}
                        key={item.index}
                        className="cursor-pointer "
                      >
                        {item.title}
                      </SLink>
                    ) : null}
                  </li>
                );
              })
            )}
          </div>
        </div>
      </div>
      <Transition.Root
        show={open}
        as={Fragment}
        style={{ zIndex: 999999999999 }}
      >
        <Dialog
          as="div"
          className="fixed inset-0 overflow-hidden"
          onClose={setOpen}
        >
          <div className="absolute inset-0 overflow-hidden">
            <Transition.Child
              as={Fragment}
              enter="ease-in-out duration-500"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="ease-in-out duration-500"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <Dialog.Overlay className="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </Transition.Child>
            <div className="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
              <Transition.Child
                as={Fragment}
                enter="transform transition ease-in-out duration-500 sm:duration-700"
                enterFrom="translate-x-full"
                enterTo="translate-x-0"
                leave="transform transition ease-in-out duration-500 sm:duration-700"
                leaveFrom="translate-x-0"
                leaveTo="translate-x-full"
              >
                <div className="pointer-events-auto relative w-screen max-w-md">
                  <Transition.Child
                    as={Fragment}
                    enter="ease-in-out duration-500"
                    enterFrom="opacity-0"
                    enterTo="opacity-100"
                    leave="ease-in-out duration-500"
                    leaveFrom="opacity-100"
                    leaveTo="opacity-0"
                  >
                    <div className="absolute top-0 left-0 -ml-8 flex pt-4 pr-2 sm:-ml-10 sm:pr-4">
                      <button
                        type="button"
                        className="rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                        onClick={() => setOpen(false)}
                      >
                        <span className="sr-only">Close panel</span>
                        <XIcon className="h-6 w-6" aria-hidden="true" />
                      </button>
                    </div>
                  </Transition.Child>
                  <div className="flex h-full flex-col overflow-y-scroll bg-white py-6 shadow-xl">
                    <div className="px-4 sm:px-6">
                      <Dialog.Title className="text-lg font-bold text-gray-900">
                        Wish List
                      </Dialog.Title>
                    </div>
                    <div className="relative mt-6 flex-1 px-4 sm:px-6">
                      <WishList
                        setOpen={setOpen}
                        asyncGetHotels={asyncGetHotels}
                      />
                    </div>
                  </div>
                </div>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition.Root>
    </>
  );
};

export default Header;
