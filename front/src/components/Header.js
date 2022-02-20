import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
    const menuItems = [
        {
            title: "Search",
            key: "/",
            index: 1,
        },
        {
            title: "Login",
            key: "/login",
            index: 2,
        },
        {
            title: "register",
            key: "/Register",
            index: 3,
        },
    ];

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
                <div className="flex">
                    {menuItems.map((item) => {
                        return (
                            <li className="list-none mx-2 p-1">
                                <Link to={item.key} key={item.index}>
                                    {item.title}
                                </Link>
                            </li>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

export default Header;
