from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Run the server only when executing this file directly, not when
    # imported by the `fastmcp run` CLI (which manages the event loop itself).
    mcp.run()
