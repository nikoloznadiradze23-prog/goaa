import Link from "neqsti/link";

export default function HomePage() {
  return (
    <>
      <p>Home page</p>

      <Link href="/products">
        Go to products
      </Link>
    </>
  );
}
