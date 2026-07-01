import asyncio
import websockets

async def echo(websocket, path):
    # This function will be called for each new WebSocket connection.
    # It receives the websocket connection object and the requested path.
    print(f"Client connected from {websocket.remote_address}")
    try:
        async for message in websocket:
            # For each message received from the client...
            print(f"Received message: {message}")
            # ...send the same message back to the client (echo).
            await websocket.send(f"Echo: {message}")
            print(f"Sent message: Echo: {message}")
    except websockets.exceptions.ConnectionClosedOK:
        print(f"Client disconnected normally from {websocket.remote_address}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Client disconnected with error from {websocket.remote_address}: {e}")
    finally:
        print(f"Connection closed for {websocket.remote_address}")

async def main():
    # Start the WebSocket server on localhost, port 8765.
    # The 'echo' function will handle incoming connections.
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        # Keep the server running indefinitely.
        await asyncio.Future()

if __name__ == "__main__":
    # Run the main asynchronous function.
    asyncio.run(main())
