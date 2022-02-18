import { atom, selector } from "recoil";

export const LoginState = atom({
    key: "LoginState",
    default: { name: "Ryan", role: "Seller" },
    dangerouslyAllowMutability: true,
});

export const searchResultState = atom({
    key: "searchResultState",
    default: ["desktop", "notebook", "smart phone", "clock", "chair", "iPad"],
    dangerouslyAllowMutability: true,
});
