# LedgerLink: Decentralized Oracle for Cryptographic Asset Pricing

LedgerLink provides a secure and decentralized mechanism for integrating real-world data, specifically cryptographic asset pricing, into blockchain applications. It leverages a network of Rust-based microservices to fetch, validate, and aggregate price data from multiple reputable exchanges. This data is then made available through a gRPC interface, providing a standardized and efficient way for smart contracts and other applications to access validated price feeds. A crucial element of LedgerLinks security model is the use of Schnorr signatures to cryptographically verify the authenticity and integrity of the data, ensuring that consumers can trust the provided information. This eliminates reliance on centralized oracles and reduces the risk of manipulation or single points of failure.

The core objective of LedgerLink is to bridge the gap between decentralized applications and the external world in a reliable and tamper-proof manner. By employing a modular microservice architecture written in Rust, LedgerLink achieves high performance and resilience. Rust's memory safety features are paramount in preventing vulnerabilities that could compromise the integrity of the oracle. The use of gRPC facilitates efficient communication between the microservices and client applications, minimizing latency and maximizing throughput. Furthermore, the integration of Schnorr signatures ensures that the data received has not been altered in transit and originates from trusted sources.

LedgerLink offers a significant advantage over traditional centralized oracles due to its decentralized nature. This decentralization fosters trust and transparency, making it ideal for high-value applications that require accurate and reliable price data. The ability to verify the data's origin and integrity through Schnorr signatures provides an added layer of security, mitigating the risk of malicious actors manipulating the data feed. By offering a robust and secure oracle solution, LedgerLink empowers developers to build more sophisticated and trustworthy decentralized applications. The project aims to contribute to a more robust and secure DeFi ecosystem.

Key Features

*   **Decentralized Data Aggregation:** LedgerLink aggregates price data from multiple independent cryptocurrency exchanges, mitigating the risk of relying on a single source of information. Each microservice independently fetches price data using secure HTTPS requests and validates it against predefined criteria, such as outlier detection.
*   **Rust-based Microservices:** The core logic of LedgerLink is implemented in Rust to leverage its memory safety features and high performance. Each microservice is designed to be modular and easily scalable, allowing the network to adapt to changing demands.
*   **gRPC Interface:** LedgerLink exposes its validated price data through a gRPC interface, providing a standardized and efficient way for clients to access the data. The gRPC protocol enables low-latency communication and supports multiple programming languages. Protocol buffer definitions are located in the `proto/` directory.
*   **Schnorr Signatures:** All price data is cryptographically signed using Schnorr signatures, ensuring its authenticity and integrity. Each microservice possesses a unique private key, and the corresponding public keys are used to verify the signatures. The signing process occurs after data validation and aggregation.
*   **Configurable Data Sources:** The list of cryptocurrency exchanges and assets tracked by LedgerLink is configurable, allowing the oracle to adapt to changing market conditions and user requirements. Configuration is managed through environment variables and configuration files.
*   **Data Validation and Filtering:** Each microservice performs data validation and filtering to ensure the accuracy and reliability of the price data. This includes outlier detection, sanity checks, and consistency checks.
*   **Python Client Library:** A Python client library is provided to simplify the integration of LedgerLink into Python-based applications and smart contracts. This library handles gRPC communication and signature verification.

Technology Stack

*   **Rust:** The core logic of the microservices is implemented in Rust, providing memory safety, performance, and reliability. Rust's strong type system and ownership model help prevent common vulnerabilities.
*   **gRPC:** gRPC is used for inter-process communication between the microservices and client applications. gRPC offers high performance, efficient serialization, and support for multiple programming languages.
*   **Protocol Buffers:** Protocol Buffers are used to define the data structures and service interfaces for gRPC. They provide a language-neutral, platform-neutral, extensible mechanism for serializing structured data.
*   **Schnorr Signatures:** Schnorr signatures are used to cryptographically verify the authenticity and integrity of the price data. The `rust-secp256k1` crate is used for signature generation and verification.
*   **Python:** The Python client library is implemented in Python, providing a convenient way for Python-based applications to interact with LedgerLink.
*   **Prometheus & Grafana:** Prometheus is used for collecting metrics from the microservices, and Grafana is used for visualizing these metrics. This allows for monitoring the health and performance of the oracle network.

Installation

1.  **Clone the repository:**
    git clone https://github.com/jjfhwang/LedgerLink.git
    cd LedgerLink

2.  **Install Rust:**
    If you don't have Rust installed, download and install it from <https://www.rust-lang.org/tools/install>.

3.  **Build the Rust microservices:**
    cd rust_microservices
    cargo build --release

4.  **Install Python dependencies:**
    cd ../python_client
    pip install -r requirements.txt

5.  **Generate gRPC stubs (if needed):**
    If you modify the `.proto` files, regenerate the gRPC stubs using the following command:
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/ledgerlink.proto

Configuration

The microservices and client library can be configured using environment variables. Here are some of the key environment variables:

*   `EXCHANGE_API_URL`: The URL of the cryptocurrency exchange API to fetch price data from (e.g., `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT`).
*   `AGGREGATION_THRESHOLD`: The minimum number of valid price data points required for aggregation.
*   `PRIVATE_KEY`: The private key used to sign the price data. This should be a hexadecimal string.
*   `GRPC_SERVER_ADDRESS`: The address of the gRPC server (e.g., `localhost:50051`).

These environment variables can be set in a `.env` file or passed directly to the microservices and client library.

Usage

Example of using the Python client library to retrieve price data:

import grpc
import ledgerlink_pb2
import ledgerlink_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = ledgerlink_pb2_grpc.PriceOracleStub(channel)
request = ledgerlink_pb2.PriceRequest(asset_pair='BTCUSDT')
response = stub.GetPrice(request)

print(f"Price: {response.price}")
print(f"Signature: {response.signature}")

This retrieves the current price of Bitcoin against USD. The `response.signature` field contains the Schnorr signature, which can be verified using the corresponding public key. Ensure that the environment variables are properly configured before running the script.

Contributing

We welcome contributions to LedgerLink! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and write tests.
4.  Submit a pull request with a detailed description of your changes.

Please ensure that your code adheres to the established coding style and that all tests pass before submitting a pull request.

License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/LedgerLink/blob/main/LICENSE) file for details.

Acknowledgements

We would like to thank the Rust and gRPC communities for providing excellent tools and resources.