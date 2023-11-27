
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.Writer;

public class MySystem {
	private static MyConsole singleton;

	public static MyConsole console() {
		if (singleton == null) {
			singleton = new MyConsole(System.in, System.out);
		}
		return singleton;
	}
}

class MyConsole {
	private BufferedReader reader;
	private PrintWriter writer;
	MyConsole(InputStream in, OutputStream out) {
		reader = new BufferedReader(new InputStreamReader(in));
		writer = new PrintWriter(out, true);
	}

	public void flush() {
		writer.flush();
	}

	public MyConsole format(String fmt, Object... args) {
		writer.format(fmt, args);
		return this;
	}

	public MyConsole printf(String format, Object... args) {
		writer.printf(format, args);
		return this;
	}

	public Reader reader() {
		return reader;
	}

	/**
	 * 各種 readLine() の実装.
	 * サーバは出力だけを見て処理するので，明示的にエコーバックする
	 * このとき，入力文字列を明示するため <i></i> で挟み込む
	 * ただしパスワード入力の場合は，エコーバックしない
	 *
	 * @param pw パスワード入力なら true, それ以外なら false
	 * @return 入力した文字列を取得
	 * */
	private String readLine(boolean pw) {
		try {
			String s = reader.readLine();
			if (s == null) {
				// 入力待ちを発生させる
				// 実行プロセスは10秒で強制終了するので15秒にしておけばオッケー
				try {
					Thread.sleep(15000);
				}
				catch (Exception e) {}
			}
			if (!pw) {
				writer.println(s);
			}
			return s;
		}
		catch (IOException e) {
			return null;
		}
	}

	public String readLine() {
		return this.readLine(false);
	}



	public String readLine(String format, Object... args) {
		writer.printf(format, args);
		return this.readLine();
	}

	public char[] readPassword() {
		return this.readLine(true).toCharArray();
	}

	public char[] readPassword(String format, Object... args) {
		writer.printf(format, args);
		return this.readPassword();
	}

	public Writer writer() {
		return writer;
	}


}
