import 'package:dartz/dartz.dart';
import '../../../../core/error/failures.dart';
import '../../domain/entities/user.dart';
import '../../domain/repositories/auth_repository.dart';
import '../datasources/auth_remote_data_source.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remoteDataSource;

  AuthRepositoryImpl({
    required this.remoteDataSource,
  });

  @override
  Future<Either<Failure, User>> signInWithEmailAndPassword(
    String email,
    String password,
  ) async {
    try {
      final user = await remoteDataSource.signInWithEmailAndPassword(
        email,
        password,
      );
      return Right(user);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Future<Either<Failure, User>> signUpWithEmailAndPassword(
    String email,
    String password,
  ) async {
    try {
      final user = await remoteDataSource.signUpWithEmailAndPassword(
        email,
        password,
      );
      return Right(user);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Future<Either<Failure, void>> signOut() async {
    try {
      await remoteDataSource.signOut();
      return const Right(null);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Future<Either<Failure, void>> sendPasswordResetEmail(String email) async {
    try {
      await remoteDataSource.sendPasswordResetEmail(email);
      return const Right(null);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Future<Either<Failure, void>> verifyEmail() async {
    try {
      await remoteDataSource.verifyEmail();
      return const Right(null);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Future<Either<Failure, User?>> getCurrentUser() async {
    try {
      final user = await remoteDataSource.getCurrentUser();
      return Right(user);
    } catch (e) {
      return Left(AuthFailure(
        message: e.toString(),
        code: 'AUTH_ERROR',
      ));
    }
  }

  @override
  Stream<User?> get authStateChanges => remoteDataSource.authStateChanges;
} 