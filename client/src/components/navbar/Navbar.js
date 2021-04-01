import React from "react";
import Link from "../link/Link";
import { NavGroup } from "./style";

const links = [
  { id: 1, to: "/", name: "home" },
  { id: 2, to: "/movies", name: "movies" },
  {
    id: 3,
    to: "/books",
    name: "books",
  },
  { id: 4, to: "/songs", name: "songs" },
  { id: 5, to: "/articles", name: "articles" },
];

const Navbar = () => {
  return (
    <div>
      <NavGroup>
        {links.map((link) => {
          return <Link to={link.to} name={link.name} key={link.id}></Link>;
        })}
      </NavGroup>
    </div>
  );
};

export default Navbar;
