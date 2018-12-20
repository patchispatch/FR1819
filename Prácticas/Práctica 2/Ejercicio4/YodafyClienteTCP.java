//
// YodafyServidorIterativo
// (CC) jjramos, 2012
//
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class YodafyClienteTCP {

	public static void main(String[] args) {

		//byte []buferEnvio;
		byte []buferEnvio=new byte[256];
		//int bytesLeidos=0;

		// Nombre del host donde se ejecuta el servidor:
		String host="localhost";
		// Puerto en el que espera el servidor:
		int port=8989;

		InetAddress direccion;
		DataramPacket paquete;

		// Socket para la conexión UDP
		Socket socket = null;
		try {
			// Creamos un socket que se conecte a "hist" y "port":
			//////////////////////////////////////////////////////
			socket = new DatagramSocket();

			//////////////////////////////////////////////////////

			//InputStream inputStream = socketServicio.getInputStream();
			//OutputStream outputStream = socketServicio.getOutputStream();

			// Si queremos enviar una cadena de caracteres por un OutputStream, hay que pasarla primero
			// a un array de bytes:
			buferEnvio="Al monte del volcán debes ir sin demora".getBytes();

			direccion = InetAddress.getByName(host);

			paquete = new DatagramPacket(buferEnvio, buferEnvio.length, direccion, port);
			socket.send(paquete);

			paquete = new DatagramPacket(buferEnvio, buferEnvio.length);
			socket.receive(paquete);

			String peticion = new String(paquete.getData(),0,paquete.getData().length);
			/////////////////////////////////////////////////////
      System.out.print(peticion);

			// Una vez terminado el servicio, cerramos el socket (automáticamente se cierran
			// el inpuStream  y el outputStream)
			//////////////////////////////////////////////////////
			socket.close();

			// Excepciones:
		} catch (UnknownHostException e) {
			System.err.println("Error: Nombre de host no encontrado.");
		} catch (IOException e) {
			System.err.println("Error de entrada/salida al abrir el socket.");
		}
	}
}
