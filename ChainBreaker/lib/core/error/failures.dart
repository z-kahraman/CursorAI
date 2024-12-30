import 'package:equatable/equatable.dart';

abstract class Failure extends Equatable {
  final String message;
  final String code;

  const Failure({
    required this.message,
    required this.code,
  });

  @override
  List<Object> get props => [message, code];
}

class ServerFailure extends Failure {
  const ServerFailure({
    required String message,
    required String code,
  }) : super(message: message, code: code);
}

class NetworkFailure extends Failure {
  const NetworkFailure({
    required String message,
    String code = 'NETWORK_ERROR',
  }) : super(message: message, code: code);
}

class AuthFailure extends Failure {
  const AuthFailure({
    required String message,
    required String code,
  }) : super(message: message, code: code);
}

class CacheFailure extends Failure {
  const CacheFailure({
    required String message,
    String code = 'CACHE_ERROR',
  }) : super(message: message, code: code);
}

class ValidationFailure extends Failure {
  const ValidationFailure({
    required String message,
    String code = 'VALIDATION_ERROR',
  }) : super(message: message, code: code);
} 