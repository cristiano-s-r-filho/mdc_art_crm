import { HydrationWrapper } from "@/components/auth/hydration-wrapper";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <HydrationWrapper>{children}</HydrationWrapper>
      </body>
    </html>
  );
}