import Link from "next/link";

const LinkText = ({ href, children, active }) => {
  return (
    <Link
      className={`font-medium ${
        active
          ? "text-indigo-100 underline underline-offset-4 decoration-indigo-600 decoration-2"
          : "hover:underline hover:underline-offset-4 hover:decoration-indigo-600 hover:decoration-2"
      }`}
      href={href}
    >
      {children === "Shows" ? (children = "TV Shows") : children}
    </Link>
  );
};

export default LinkText;
