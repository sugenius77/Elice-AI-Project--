import React from "react";
import Header from "components/Header";
import Footer from "components/Footer";

const Layout = ({ children }) => {
    return (
        <div>
            {/* <Header /> */}
            <div className="content overflow-x-hidden">{children}</div>
            <Footer />
        </div>
    );
};

export default Layout;
